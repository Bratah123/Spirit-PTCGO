from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive


class DarknessGuardPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.target is carrier):
            return
        if any(
            energy_provides_type(c, PokemonTypes.DARKNESS.value)
            for c in carrier.children
        ):
            calc.amount = max(0, calc.amount - 20)


card = PokemonCardDef(
    guid="ff8b5d90-1361-5b57-9ebb-6a33f87e61ec",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Ability(
            title="Darkness Guard",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached, it takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=DarknessGuardPassive(),
        ),
        Attack(
            title="Vortex of Darkness",
            game_text="This attack does 20 more damage for each Darkness Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.DARKNESS), 20, base=60
            ),
        ),
    ],
)