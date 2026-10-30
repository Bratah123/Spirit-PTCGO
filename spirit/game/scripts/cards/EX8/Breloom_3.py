"""STUB: effect not implemented — do not guess mechanics.
Breloom (EX8 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import hustle_punch_next, leaf_poison_if_grass


card = PokemonCardDef(
    guid="71c5fa53-2196-59e9-a794-bcd8fe881b81",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Leaf Poison",
            game_text="If Breloom has any Grass Energy attached to it, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=leaf_poison_if_grass(),
        ),
        Attack(
            title="Hustle Punch",
            game_text="During your next turn, Hustle Punch attack's base damage is 50 instead of 70.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=hustle_punch_next(),
        ),
    ],
)