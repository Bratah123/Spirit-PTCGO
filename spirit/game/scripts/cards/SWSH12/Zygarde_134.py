from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18232951-426c-5481-a3d1-9a4b9f349b5f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=718,
    abilities=[
        Attack(
            title="Shout of Power",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)