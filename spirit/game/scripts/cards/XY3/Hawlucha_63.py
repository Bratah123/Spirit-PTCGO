from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for


class _ShiningSpirit(Passive):
    """Damage from this Pokemon's attacks isn't affected by W/R."""
    def modify_weakness(self, calc, carrier):
        if calc.attacker is not None and calc.attacker is carrier_pokemon(carrier):
            calc.weakness_applies = False

    def modify_resistance(self, calc, carrier):
        if calc.attacker is not None and calc.attacker is carrier_pokemon(carrier):
            calc.resistance_applies = False


async def _flying_press(ctx):
    """60; does nothing unless the opponent's Active is a Pokemon-EX."""
    target = ctx.defender
    if target is not None and "EX" in (getattr(def_for(target.archetype_id), "subtypes", None) or []):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="589cda6d-cf8f-5120-9766-0f80057d6e7e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Ability(
            title="Shining Spirit",
            game_text="Damage from this Pok\u00e9mon's attacks isn't affected by Weakness or Resistance.",
            passive=_ShiningSpirit(),
        ),
        Attack(
            title="Flying Press",
            game_text="If your opponent's Active Pok\u00e9mon isn't a Pok\u00e9mon-EX, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=_flying_press,
        ),
    ],
)