from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17ec4cdd-2663-5f6b-8d28-a2af4f3b9f52",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFini.Name",
    display_name="Tapu Fini",
    searchable_by=["Tapu Fini", "Basic", "Rapid Strike", "TapuFini"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=40,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=788,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Ocean Loop",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)