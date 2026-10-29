from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import dead_end_gx, restoration, restoration_condition


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="09c4eaab-9238-5512-b696-0da3d5c18ad8",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiGX.Name",
    display_name="Darkrai-GX",
    searchable_by=["Darkrai-GX", "Basic", "GX", "DarkraiGX"],
    subtypes=["Basic", "GX"],
    collector_number=88,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title="Restoration",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. Then, attach a Darkness Energy card from your discard pile to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=restoration_condition,
            effect=restoration,
        ),
        Attack(
            title="Dark Cleave",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=feint,
        ),
        Attack(
            title="Dead End-GX",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=dead_end_gx,
        ),
    ],
)
