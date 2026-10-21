from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


async def _bite(ctx):
    """When played from hand to evolve: you may put 3 damage counters on 1
    of your opponent's Pokemon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets or not await ctx.ask_yes_no(
            "Put 3 damage counters on 1 of your opponent's Pokémon?"):
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Put damage counters on which Pokémon?")
    await ctx.deal_damage(30, target=target or targets[0], apply_modifiers=False,
                          is_attack=False, as_counters=True)


card = PokemonCardDef(
    guid="e2a9e7db-36c1-5c00-a2ae-f3a4e34db1fa",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Surprise Bite",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_bite,
        ),
        Attack(
            title="Skill Dive",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(30, pool='any', count=1),
        ),
    ],
)