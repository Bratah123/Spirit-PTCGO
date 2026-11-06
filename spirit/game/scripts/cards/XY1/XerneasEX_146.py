from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="0a4df5e7-3a87-5238-af82-9f78b88486f9",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XerneasEX.Name",
    display_name="Xerneas-EX",
    searchable_by=["Xerneas-EX", "Basic", "EX", "XerneasEX"],
    subtypes=["Basic", "EX"],
    collector_number=146,
    set_code="XY1",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Break Through",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="X Blast",
            game_text="This Pok\u00e9mon can't use X Blast during your next turn.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)