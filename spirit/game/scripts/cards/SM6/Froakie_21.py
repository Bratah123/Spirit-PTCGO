from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import frubbles_passive

card = PokemonCardDef(
    guid="ae4d62a9-8b6d-5684-91f7-f022190d9a8a",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic", "Froakie"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=656,
    abilities=[
        Ability(
            title="Frubbles",
            game_text="If this Pok\u00e9mon has any Water Energy attached to it, it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=frubbles_passive,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
