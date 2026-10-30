from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import energy_powder


card = PokemonCardDef(
    guid="7cc49652-1afa-546a-a22c-91687bc15485",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Energy Powder",
            game_text="Search your deck for up to 2 basic Energy cards and attach them to any of your Pok\u00e9mon (excluding Pok\u00e9mon-ex) in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=energy_powder(),
        ),
        Attack(
            title="Toxic Spore",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)