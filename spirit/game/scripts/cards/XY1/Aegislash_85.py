from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import stance_change, stance_change_condition


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="925ea705-f326-5332-8536-8f484111f325",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Stance Change",
            game_text="Once during your turn (before your attack), you may switch this Pok\u00e9mon with an Aegislash in your hand. (Any cards attached to this Pok\u00e9mon, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=stance_change_condition,
            effect=stance_change,
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=feint,
        ),
    ],
)