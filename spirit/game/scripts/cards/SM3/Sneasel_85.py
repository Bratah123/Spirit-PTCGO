from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn

card = PokemonCardDef(
    guid="da786fba-5592-5552-8214-360a10c599e5",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title="Hone Claws",
            game_text="During your next turn, this Pok\u00e9mon's Slash attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(60, attack_title='Slash'),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
