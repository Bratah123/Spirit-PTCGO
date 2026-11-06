from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="f24b88a9-f474-5384-b100-1ed5e979fbf8",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1", "Metapod"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="All damage done by attacks to Metapod is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
