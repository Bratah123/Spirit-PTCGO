from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _lightning_symbol_attacker(p):
    if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Zapdos":
        return False
    if p.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
        return False
    return PokemonTypes.LIGHTNING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="c6aa5471-9004-56f0-8f14-8ecad787bf37",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Lightning Symbol",
            game_text="Your Basic Lightning Pok\u00e9mon's attacks, except any Zapdos, do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(10, attacker_pred=_lightning_symbol_attacker),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)