from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import remove_self_from_play
from spirit.game.card_effects.sm4 import blade_gx, slice_off

card = PokemonCardDef(
    guid="a6dc3316-048f-5078-86c1-2d19df322953",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KartanaGX.Name",
    display_name="Kartana-GX",
    searchable_by=["Kartana-GX", "Basic", "GX", "Ultra Beast", "KartanaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=142,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=798,
    abilities=[
        Ability(
            title="Slice Off",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Special Energy from 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=slice_off,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Gale Blade",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=remove_self_from_play('deck', optional=True),
        ),
        Attack(
            title="Blade-GX",
            game_text="Take a Prize card. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=blade_gx,
        ),
    ],
)