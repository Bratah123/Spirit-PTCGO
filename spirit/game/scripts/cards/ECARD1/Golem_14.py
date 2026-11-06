from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.ecard import rock_tumble


card = PokemonCardDef(
    guid="600e5df8-62e6-5848-bdb6-97bae410d401",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Ability(
            title="Rock Body",
            game_text="All damage done by attacks to Golem is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=takes_less_passive(10),
        ),
        Attack(
            title="Rock Tumble",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=rock_tumble,
        ),
    ],
)
