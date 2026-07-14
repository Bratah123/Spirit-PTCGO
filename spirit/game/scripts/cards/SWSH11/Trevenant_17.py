from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class ElderTreeBarrierPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier or not ctx.is_attack_effect():
            return count
        attacker = ctx.attacker
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if not is_pokemon_v(attacker.archetype_id):
            return count
        return 0


card = PokemonCardDef(
    guid="19554151-d920-58d3-bd38-1fa326759400",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Ability(
            title="Elder Tree Barrier",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon V, your opponent can't take any Prize cards for it.",
            passive=ElderTreeBarrierPassive(),
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            locks_next_turn=True,
        ),
    ],
)