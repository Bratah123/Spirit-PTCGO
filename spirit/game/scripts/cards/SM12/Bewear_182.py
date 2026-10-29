from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import retreat_discount, is_in_active_spot
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="e0fa0835-0507-57b9-8f4b-75cf45e3cc0e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=182,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Ability(
            title="Carry and Run",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Active Pok\u00e9mon's Retreat Cost is ColorlessColorless less.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=retreat_discount(2, target_pred=lambda pokemon, carrier: pokemon.owning_player_id == carrier.owning_player_id and is_in_active_spot(pokemon) and (not is_in_active_spot(carrier))),
        ),
        Attack(
            title="Lariat",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=flip_or_nothing(),
        ),
    ],
)