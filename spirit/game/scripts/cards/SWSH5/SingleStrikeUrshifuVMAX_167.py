from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b53ae03b-3831-58e6-82a1-af37317ef96c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuVMAX.Name",
    display_name="Single Strike Urshifu VMAX",
    searchable_by=["Single Strike Urshifu VMAX", "VMAX", "Single Strike", "SingleStrikeUrshifuVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=167,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name",
    family_id=892,
    abilities=[
        Attack(
            title="Beatdown",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="G-Max One Blow",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=270,
            effect=unimplemented,
        ),
    ],
)