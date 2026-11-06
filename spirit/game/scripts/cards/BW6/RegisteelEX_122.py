from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="2b40d02f-9532-5cc1-8f56-43c8e4754ec4",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegisteelEX.Name",
    display_name="Registeel-EX",
    searchable_by=["Registeel-EX", "Basic", "EX", "RegisteelEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Attack(
            title="Triple Laser",
            game_text="This attack does 30 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon).",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(30, pool='any', count=3),
        ),
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)