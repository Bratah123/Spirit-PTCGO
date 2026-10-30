from spirit.game.card_effects.ex import energy_link_self, darkness_veil_effects_passive
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Articuno ex (EX7 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=darkness_veil_effects_passive(),
    guid="f9f4cf21-e9c2-5028-aab5-8289c66561b5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsArticunoex.Name",
    display_name="Rocket's Articuno ex",
    searchable_by=["Rocket's Articuno ex", "Basic", "ex", "RocketsArticunoex"],
    subtypes=["Basic", "ex"],
    collector_number=96,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Darkness Veil",
            game_text="As long as Rocket's Articuno ex has any Darkness Energy attached to it, prevent all effects, except damage, by an opponent's attack done to Rocket's Articuno ex.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Freeze Solid",
            game_text="Search your discard pile for a Water Energy card and attach it to Rocket's Articuno ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=energy_link_self(PokemonTypes.WATER),
        ),
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)