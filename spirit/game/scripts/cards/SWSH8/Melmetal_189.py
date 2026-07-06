from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c6c77afc-4ec7-5cbf-88f7-62f24ec7a247",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Single Strike", "Melmetal"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=189,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Ingot Swing",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon that have an Ability.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Blasting Hammer",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)