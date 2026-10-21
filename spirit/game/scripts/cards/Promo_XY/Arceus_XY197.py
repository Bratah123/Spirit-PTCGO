from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive, carrier_pokemon


_TYPE_CHOICES = [PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING,
                 PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING, PokemonTypes.DARKNESS, PokemonTypes.METAL,
                 PokemonTypes.FAIRY, PokemonTypes.DRAGON]


class _TypeSwitched(Passive):
    """Until the end of your next turn, this Pokemon is the chosen type."""
    def __init__(self, type_value):
        self.type_value = type_value

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [self.type_value]


async def _type_switch(ctx):
    """Choose a type; until the end of your next turn this Pokemon is that type."""
    labels = [t.name.capitalize() for t in _TYPE_CHOICES]
    pick = await ctx.choose("Choose a type for this Pokémon", labels)
    if pick is None or not 0 <= pick < len(_TYPE_CHOICES):
        return
    ctx.add_passive_through_own_next_turn(ctx.attacker, _TypeSwitched(_TYPE_CHOICES[pick].value))


card = PokemonCardDef(
    guid="84a75418-085b-55d4-9836-602f88d5a80a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=197,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Type Switch",
            game_text="Choose Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal, Fairy, or Dragon type. Until the end of your next turn, this Pok\u00e9mon is that type.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_type_switch,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)