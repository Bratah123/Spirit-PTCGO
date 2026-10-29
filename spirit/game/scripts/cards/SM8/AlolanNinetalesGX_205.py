from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    mysterious_guidance,
    snowy_wind,
    sublimation_gx,
)

card = PokemonCardDef(
    guid="d392fe75-50e3-5379-b207-ad7b9c2c15cc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetalesGX.Name",
    display_name="Alolan Ninetales-GX",
    searchable_by=["Alolan Ninetales-GX", "Stage 1", "GX", "AlolanNinetalesGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=205,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Mysterious Guidance",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=mysterious_guidance,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Snowy Wind",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=snowy_wind
        ),
        Attack(
            title="Sublimation-GX",
            game_text="If your opponent's Active Pok\u00e9mon is an Ultra Beast, it is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=sublimation_gx
        ),
    ],
)