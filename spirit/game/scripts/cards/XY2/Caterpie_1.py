from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="ed979b4d-96e0-5563-9ddf-7511de4b931a",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic", "Caterpie"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)