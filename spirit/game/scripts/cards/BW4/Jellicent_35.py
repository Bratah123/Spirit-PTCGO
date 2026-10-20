from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


async def _vengeful_wish(ctx):
    """Deal the damage this Pokémon took from attacks last turn."""
    amount = ctx.damage_taken_last_turn(ctx.attacker)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="34cb27b9-94a7-5646-8c94-bcfdc949431b",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Attack(
            title="Vengeful Wish",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does the same amount of damage done to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_vengeful_wish,
        ),
        Attack(
            title="Absorb Life",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
    ],
)