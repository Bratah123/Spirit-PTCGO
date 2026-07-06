from spirit.game.card_effects.pokemon import cross_fusion_strike, max_miracle
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7bbdd12-2615-5812-97c3-4560a7c991bc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewVMAX.Name",
    display_name="Mew VMAX",
    searchable_by=["Mew VMAX", "VMAX", "Fusion Strike", "MewVMAX"],
    subtypes=["VMAX", "Fusion Strike"],
    collector_number=269,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewV.Name",
    family_id=151,
    abilities=[
        Attack(
            title="Cross Fusion Strike",
            game_text="Choose 1 of your Benched Fusion Strike Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=cross_fusion_strike,
        ),
        Attack(
            title="Max Miracle",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=max_miracle,
        ),
    ],
)