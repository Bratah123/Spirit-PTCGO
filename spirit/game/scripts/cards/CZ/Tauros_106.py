from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage

card = PokemonCardDef(
    guid="526514b5-22a1-5a59-9466-a59108ab2d91",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Adrena-Tackle",
            game_text="If this Pok\u00e9mon has no damage counters on it, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=bonus_if(has_damage("self"), 0, else_nothing=True),
        ),
    ],
)