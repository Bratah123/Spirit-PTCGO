from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

async def overspin(ctx):
    state = ctx.session.turn_state
    if state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number:
        return
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="d8257185-61f7-530f-b2a3-257539d319a7",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toucannon.Name",
    display_name="Toucannon",
    searchable_by=["Toucannon", "Stage 2", "Toucannon"],
    subtypes=["Stage 2"],
    collector_number=166,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    family_id=731,
    abilities=[
        Attack(
            title="Heat Beak",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Giganticannon",
            game_text="If this Pok\u00e9mon evolved during this turn, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=overspin,
        ),
    ],
)