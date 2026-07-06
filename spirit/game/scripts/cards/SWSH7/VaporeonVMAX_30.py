from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45eb2749-287c-571c-8b28-bfd418da7845",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonVMAX.Name",
    display_name="Vaporeon VMAX",
    searchable_by=["Vaporeon VMAX", "VMAX", "Rapid Strike", "VaporeonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=30,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonV.Name",
    family_id=134,
    abilities=[
        Attack(
            title="Bubble Pod",
            game_text="Put a Water Pok\u00e9mon from your discard pile onto your Bench. If you do, attach up to 3 Water Energy cards from your discard pile to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Torrent",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)