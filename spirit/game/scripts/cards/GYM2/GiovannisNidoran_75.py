from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, recoil_attack


card = PokemonCardDef(
    guid="39abcbb3-6bac-5c28-8e05-9b92793ba027",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    display_name="Giovanni's Nidoran ♀",
    searchable_by=["Giovanni's Nidoran \u2640", "Basic", "GiovannisNidoran"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Horn Thrust",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Double-edge",
            game_text="Giovanni's Nidoran \u2640 does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=recoil_attack(20),
        ),
    ],
)
