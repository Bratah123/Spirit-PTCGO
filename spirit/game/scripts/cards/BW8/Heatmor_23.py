from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="140e4025-a3a1-5cf7-b0e2-441cccdd9cb0",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Luring Flame",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fiery Licks",
            game_text="Discard the top 4 cards of your deck. This attack does 50 damage times the number of Fire Energy cards discarded.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)