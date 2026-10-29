from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.support_common import remove_self_from_play
from spirit.game.card_effects.sm6 import shadowy_hunter_gx, shuriken_flurry

card = PokemonCardDef(
    guid="3d4f910e-d823-5a9e-849e-7de8a0458e8e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name",
    display_name="Greninja-GX",
    searchable_by=["Greninja-GX", "Stage 2", "GX", "GreninjaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=24,
    set_code="SM6",
    rarity=Rarities.RareHoloGX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Shuriken Flurry",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=shuriken_flurry,
        ),
        Attack(
            title="Haze Slash",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=remove_self_from_play('deck', optional=True),
        ),
        Attack(
            title="Shadowy Hunter-GX",
            game_text="This attack does 130 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=shadowy_hunter_gx,
        ),
    ],
)
