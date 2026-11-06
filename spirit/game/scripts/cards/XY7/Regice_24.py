from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for


async def _resistance_desert(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _ResistanceDesert())


class _ResistanceDesert(Passive):
    """Prevent all damage done to this Pokemon by attacks from Pokemon-EX."""
    def prevents_damage(self, calc, carrier):
        a = calc.attacker
        return (calc.is_attack and calc.target is carrier_pokemon(carrier) and a is not None
                and "EX" in (getattr(def_for(a.archetype_id), "subtypes", None) or []))


card = PokemonCardDef(
    guid="c633e271-f118-52f9-814d-a2a251a7e10f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Resistance Blizzard",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_resistance_desert,
        ),
    ],
)