from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="3be5e123-a71d-5734-8d0f-97ce182d7320",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    display_name="Fomantis",
    searchable_by=["Fomantis", "Basic", "Fomantis"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=753,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(30, 'choice'),
        ),
        Attack(
            title="Leafage",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)