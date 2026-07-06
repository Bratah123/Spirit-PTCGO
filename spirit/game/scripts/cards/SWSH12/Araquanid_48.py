from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a64cf849-dc93-5c33-af8e-7a7f496cfa05",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name",
    display_name="Araquanid",
    searchable_by=["Araquanid", "Stage 1", "Araquanid"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    family_id=751,
    abilities=[
        Attack(
            title="Drowning Ball",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed, and discard an Energy from that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)