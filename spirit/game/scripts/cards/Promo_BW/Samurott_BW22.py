from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="afb048b3-5044-5088-85f9-e3e47287c7fd",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2", "Samurott"],
    subtypes=["Stage 2"],
    collector_number=22,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Shell Armor",
            game_text="Any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 10 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.WATER), 10, base=70,
            ),
        ),
    ],
)
