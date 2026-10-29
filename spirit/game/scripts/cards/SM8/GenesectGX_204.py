from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import muscle_punch_gx

from spirit.game.card_effects.sm8 import (
    double_drive_passive,
)

card = PokemonCardDef(
    guid="88773070-88e2-59ea-aa6f-ed8b3fd56d54",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectGX.Name",
    display_name="Genesect-GX",
    searchable_by=["Genesect-GX", "Basic", "GX", "GenesectGX"],
    subtypes=["Basic", "GX"],
    collector_number=204,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Ability(
            title="Double Drive",
            game_text="This Pok\u00e9mon may have up to 2 Pok\u00e9mon Tool cards attached to it. If it loses this Ability, discard Pok\u00e9mon Tool cards from it until only 1 remains.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=double_drive_passive
        ),
        Attack(
            title="Burst Shot",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Break Buster-GX",
            game_text="This attack's damage isn't affected by Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=muscle_punch_gx,
        ),
    ],
)