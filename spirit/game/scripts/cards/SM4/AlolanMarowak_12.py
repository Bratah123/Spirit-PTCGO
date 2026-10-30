from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import burning_bonemerang, dance_of_flames

card = PokemonCardDef(
    guid="94a6977f-b587-570d-9014-692268f1958a",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1", "AlolanMarowak"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Dance of Flames",
            game_text="For each Energy attached to your opponent's Pok\u00e9mon, attach a Fire Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={},
            effect=dance_of_flames,
        ),
        Attack(
            title="Burning Bonemerang",
            game_text="Flip 2 coins. This attack does 70 damage for each heads. If either of them is heads, your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=burning_bonemerang,
        ),
    ],
)