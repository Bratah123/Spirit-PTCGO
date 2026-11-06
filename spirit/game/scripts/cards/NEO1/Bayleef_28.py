from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import pollen_shield


card = PokemonCardDef(
    guid="c02b8406-49e2-56be-9472-5e71ac2850b4",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    display_name="Bayleef",
    searchable_by=["Bayleef", "Stage 1", "Bayleef"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    family_id=152,
    abilities=[
        Attack(
            title="Poisonpowder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Pollen Shield",
            game_text="During your opponent's next turn, Bayleef can't become Asleep, Confused, Paralyzed, or Poisoned. (All other effects of attacks, Pok\u00e9mon Powers and Trainer cards still happen.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=pollen_shield,
        ),
    ],
)
