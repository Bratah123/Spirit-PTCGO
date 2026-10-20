from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="a1ad14c2-4f24-561e-94f3-6da6bd11eb07",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=39,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)