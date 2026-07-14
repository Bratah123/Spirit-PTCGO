from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class NoEvolveDefenderPassive(Passive):
    def blocks_evolution(self, player_id, target, carrier):
        return target is carrier and player_id == carrier.owning_player_id


async def bone_block(ctx):
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(defender, NoEvolveDefenderPassive())


card = PokemonCardDef(
    guid="f81b344d-44ea-5465-9d48-e6414b2af7bc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1", "Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=173,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Bone Block",
            game_text="During your opponent's next turn, Pok\u00e9mon can't be played from your opponent's hand to evolve the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=bone_block,
        ),
        Attack(
            title="Dark Cutter",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)