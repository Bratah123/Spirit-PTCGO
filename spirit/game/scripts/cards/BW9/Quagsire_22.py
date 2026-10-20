from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.attacks_common import bonus_if, count_energy


_fighting_energy = count_energy("self", energy_type=PokemonTypes.FIGHTING)


card = PokemonCardDef(
    guid="6c70ddc1-425d-5d2c-addb-4d7b2f5e847c",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Laid-Back",
            game_text="Any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Mud Gun",
            game_text="If this Pok\u00e9mon has any Fighting Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: _fighting_energy(ctx) > 0, 30),
        ),
    ],
)