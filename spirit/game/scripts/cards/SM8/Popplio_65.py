from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="ec46de5c-7382-5fbd-9542-fd3862178e7a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    display_name="Popplio",
    searchable_by=["Popplio", "Basic", "Popplio"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=728,
    abilities=[
        Attack(
            title="Blot",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)