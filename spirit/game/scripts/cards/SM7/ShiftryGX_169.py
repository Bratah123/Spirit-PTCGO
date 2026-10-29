from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm7 import (
    den_of_iniquity_gx,
    extrasensory,
)


card = PokemonCardDef(
    guid="e7801b9c-d048-5607-afae-f76ee0254bd0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiftryGX.Name",
    display_name="Shiftry-GX",
    searchable_by=["Shiftry-GX", "Stage 2", "GX", "ShiftryGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=169,
    set_code="SM7",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=extrasensory,
        ),
        Attack(
            title="Den of Iniquity-GX",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Your opponent shuffles that Pok\u00e9mon and all cards attached to it into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=den_of_iniquity_gx,
        ),
    ],
)