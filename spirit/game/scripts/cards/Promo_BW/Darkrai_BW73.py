from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="9cfc646b-ab78-5d10-9fde-fbda9927697c",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Team Plasma", "Darkrai"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=73,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Attack(
            title="Hide in Shadows",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Dark Hole",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)