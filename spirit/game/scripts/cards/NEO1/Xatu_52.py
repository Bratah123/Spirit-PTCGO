from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import foresight


card = PokemonCardDef(
    guid="f254c3f0-405c-5b0e-9ed0-5bf44efc1e08",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Prophecy",
            game_text="Look at the top 3 cards of either player's deck and rearrange them as you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=foresight,
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
