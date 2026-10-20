from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="afff7b10-759d-5290-ae1f-fb44ad5040da",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Team Plasma", "Genesect"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=86,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Attack(
            title="Signal Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=boost_own_next_turn(60, attack_title='Overdrive Smash'),
        ),
    ],
)