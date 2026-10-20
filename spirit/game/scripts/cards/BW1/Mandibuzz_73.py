from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_stage2_pokemon


async def blindside(ctx):
    """50 damage to 1 of your opponent's Pokémon that has damage counters."""
    candidates = [
        p for p in ctx.opponent_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with damage counters",
    )
    if target is not None:
        await ctx.deal_damage(50, target=target)


card = PokemonCardDef(
    guid="0c5d265d-7eb2-5a0c-8ea7-9c1a916f762b",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1", "Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Blindside",
            game_text="Does 50 damage to 1 of your opponent's Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=blindside,
        ),
        Attack(
            title="Punishment",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(active_is(is_stage2_pokemon), 60),
        ),
    ],
)
