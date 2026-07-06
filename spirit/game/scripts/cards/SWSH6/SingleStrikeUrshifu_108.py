from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77b3671c-2b08-5330-a74d-c31c47a2c74a",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifu.Name",
    display_name="Single Strike Urshifu",
    searchable_by=["Single Strike Urshifu", "Stage 1", "Single Strike", "SingleStrikeUrshifu"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=108,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kubfu.Name",
    family_id=891,
    abilities=[
        Attack(
            title="Field Crush",
            game_text="If your opponent has a Stadium in play, discard it.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Fists of Strife",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)