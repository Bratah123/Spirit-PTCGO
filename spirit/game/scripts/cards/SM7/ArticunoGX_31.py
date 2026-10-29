from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    cold_crush_gx,
    legendary_ascent,
)
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="3462e313-dfa4-5150-9e50-d114dcf0eeda",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArticunoGX.Name",
    display_name="Articuno-GX",
    searchable_by=["Articuno-GX", "Basic", "GX", "ArticunoGX"],
    subtypes=["Basic", "GX"],
    collector_number=31,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Legendary Ascent",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may switch it with your Active Pok\u00e9mon. If you do, move any number of Water Energy from your other Pok\u00e9mon to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=legendary_ascent,
        ),
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Cold Crush-GX",
            game_text="Discard all Energy from both Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=cold_crush_gx,
        ),
    ],
)