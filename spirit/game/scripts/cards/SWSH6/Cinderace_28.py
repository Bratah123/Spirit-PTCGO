from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.session.passives import Passive


class CrisisPowerPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if calc.attacker is not carrier:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        opponent = next(
            (p for p in calc.board.player_ids if p != carrier.owning_player_id), None
        )
        if opponent is None:
            return
        bonus = 30 * calc.board.prizes_taken(opponent)
        if bonus:
            calc.amount += bonus


async def fireball_shot(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="96ee16d4-f31f-5ef0-a193-a69d8f7cab4b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Single Strike", "Cinderace"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=28,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Ability(
            title="Crisis Power",
            game_text="This Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon for each Prize card your opponent has taken (before applying Weakness and Resistance).",
            passive=CrisisPowerPassive(),
        ),
        Attack(
            title="Fireball Shot",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=fireball_shot,
        ),
    ],
)