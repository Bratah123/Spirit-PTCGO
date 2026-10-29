from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.sm5 import flashing_head_passive, lighting_gx

card = PokemonCardDef(
    guid="8c3e6ca5-5c7c-5799-b090-759c8f562e0b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XurkitreeGX.Name",
    display_name="Xurkitree-GX",
    searchable_by=["Xurkitree-GX", "Basic", "GX", "Ultra Beast", "XurkitreeGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=68,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=796,
    abilities=[
        Ability(
            title="Flashing Head",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have any Special Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=flashing_head_passive,
        ),
        Attack(
            title="Rumbling Wires",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=mill_attack(1),
        ),
        Attack(
            title="Lighting-GX",
            game_text="Your opponent reveals their hand. Add a card you find there to their Prize cards face down. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=lighting_gx,
        ),
    ],
)