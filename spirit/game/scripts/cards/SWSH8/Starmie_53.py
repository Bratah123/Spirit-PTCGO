from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70fbca44-48d0-572a-adf0-0221f686394c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Rapid Strike", "Starmie"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=53,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Multishot Star",
            game_text="Discard any amount of Water Energy from this Pok\u00e9mon. Then, for each Energy card you discarded in this way, choose 1 of your opponent's Pok\u00e9mon and do 30 damage to it. (You can choose the same Pok\u00e9mon more than once.) This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)