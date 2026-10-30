from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.sm3 import eternal_flame_gx


card = PokemonCardDef(
    guid="d192839d-843c-5e19-885c-c1ade1dc4e4a",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name",
    display_name="Ho-Oh-GX",
    searchable_by=["Ho-Oh-GX", "Basic", "GX", "HoOhGX"],
    subtypes=["Basic", "GX"],
    collector_number=131,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Fire",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=snipe_attack(50, pool='any', count=1),
        ),
        Attack(
            title="Phoenix Burn",
            game_text="This Pok\u00e9mon can't use Phoenix Burn during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            locks_next_turn=True,
        ),
        Attack(
            title="Eternal Flame-GX",
            game_text="Put 3 in any combination of Fire Pok\u00e9mon-GX or Fire Pok\u00e9mon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=eternal_flame_gx,
        ),
    ],
)
